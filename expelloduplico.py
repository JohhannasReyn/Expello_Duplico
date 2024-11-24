import sublime
import sublime_plugin
import re

class ExpelloduplicoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("ExpelloduplicoCommand triggered.")  # Debug

        # Load settings
        settings = sublime.load_settings("expelloduplico.sublime-settings")
        delimiters = settings.get("delimiters", ["\n", ",", ";", " "])
        threshold = settings.get("threshold", 4)
        action = settings.get("do_with_duplicates_found", "selecto")
        print(f"Settings loaded - Delimiters: {delimiters}, Threshold: {threshold}, Action: {action}")  # Debug

        # Process each region or entire document if no selection
        regions = self.view.sel()
        if all(region.empty() for region in regions):
            print("No text selected; applying to the entire document.")  # Debug
            regions = [sublime.Region(0, self.view.size())]  # Entire document as a region

        for region in regions:
            text = self.view.substr(region)
            print(f"Processing region: {text[:50]}...")  # Debug (truncate long text for readability)

            # Determine the delimiter
            delimiter = self.detect_delimiter(text, delimiters, threshold)
            if not delimiter:
                print("No delimiter met the threshold; skipping region.")  # Debug
                continue

            print(f"Detected delimiter: {repr(delimiter)}")  # Debug

            # Handle duplicates based on user preference
            if action == "selecto":
                self.select_duplicates(region, text, delimiter)
            elif action == "expello":
                self.remove_duplicates(edit, region, text, delimiter)

    def detect_delimiter(self, text, delimiters, threshold):
        print("Detecting delimiter...")  # Debug
        for delimiter in delimiters:
            count = len(re.findall(re.escape(delimiter), text))  # Count occurrences of the delimiter
            print(f"Delimiter: {repr(delimiter)}, Count: {count}")  # Debug
            if count >= threshold:
                return delimiter
        return None

    def remove_duplicates(self, edit, region, text, delimiter):
        print(f"Removing duplicates with delimiter: {repr(delimiter)}")  # Debug
        items = text.split(delimiter)
        unique_items = list(dict.fromkeys(item.strip() for item in items))  # Maintain order
        result = delimiter.join(unique_items)
        print(f"Resulting text: {result[:50]}...")  # Debug (truncate long result for readability)
        self.view.replace(edit, region, result)

    def select_duplicates(self, region, text, delimiter):
        print(f"Selecting duplicates with delimiter: {repr(delimiter)}")  # Debug
        items = text.split(delimiter)
        seen = set()
        duplicates = []

        # Identify duplicates (skip first occurrence)
        for i, item in enumerate(items):
            stripped = item.strip()
            if stripped in seen:
                duplicates.append((i, stripped))
            else:
                seen.add(stripped)

        print(f"Duplicate entries found: {duplicates}")  # Debug

        # Highlight duplicates in the view
        new_regions = []
        start = region.begin()
        for i, duplicate in duplicates:
            # Compute start/end positions of the duplicate item
            pos = start + sum(len(items[j]) + len(delimiter) for j in range(i))
            length = len(duplicate)
            new_regions.append(sublime.Region(pos, pos + length))

        self.view.sel().clear()
        for duplicate_region in new_regions:
            self.view.sel().add(duplicate_region)
        print(f"Highlighted {len(new_regions)} duplicates.")  # Debug
