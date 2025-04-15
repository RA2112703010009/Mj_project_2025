import re 


#logs page functions 
# Import regex module for case-insensitive matching

class LogViewer:
    def __init__(self, logs):
        self.logs = logs

    def search_logs(self, search_term):
        """Search logs, change highlighted text to black while keeping the background changed to yellow."""
        if not search_term.strip():
            return self.logs, "Search term cannot be empty."
        
        search_term = search_term.strip()
        # Use regex for case-insensitive replacement
        regex = re.compile(re.escape(search_term), re.IGNORECASE)
        
        if regex.search(self.logs):
            # Wrap the matched text in a span that changes only text color
            highlighted_logs = regex.sub(
                f'<span style="background-color: yellow; color: black;">{search_term}</span>',
                self.logs
            )
            message = f'Search term \"{search_term}\" found.'
        else:
            highlighted_logs = self.logs
            message = f'Search term \"{search_term}\" not found in logs.'
        
        return highlighted_logs, message




    

