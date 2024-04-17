def canUnlockAll(boxes):
    """
    Determines whether all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes. Each inner list contains positive integer keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize the list of unlocked boxes with the first box (index 0)
    unlocked = [0]

    # Iterate through the keys in each box
    for box_index in unlocked:
        for key in boxes[box_index]:
            # If the key is not already in the unlocked list and it's a valid box index
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
