import os


def clean_blank_text_files(directory='.'):  # Default to current directory mninnihohuh
    """Append .tmp to all blank text files (.txt) in the specified directory instead of removing them."""
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            try:
                if os.path.getsize(filepath) == 0:
                    new_filepath = filepath + '.tmp'
                    os.rename(filepath, new_filepath)
                    print(f"Renamed blank file: {filepath} -> {new_filepath}")
            except OSError as e:
                print(f"Error processing file {filepath}: {e}")


if __name__ == '__main__':
    clean_blank_text_files()
