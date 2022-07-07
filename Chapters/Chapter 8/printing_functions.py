def print_models(to_print, completed):
    """
    Simulates printing models from the to_print list and moving completed
    models to the completed list.
    """
    while to_print:
        model = to_print.pop()
        print(f"Printing {model}...")
        completed.append(model)

def print_summary(completed):
    """Prints a summary of completed printing"""
    print("The following items were printed: ")
    for model in completed:
        print(f" - {model}")
