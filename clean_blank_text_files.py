import os


def clean_blank_text_files(directory='.'):  # Default to current directory
    """Remove all blank text files (.txt) in the specified directory."""
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            try:
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath)
                    print(f"Removed blank file: {filepath}")
            except OSError as e:
                print(f"Error processing file {filepath}: {e}")


if __name__ == '__main__':
    clean_blank_text_files()
