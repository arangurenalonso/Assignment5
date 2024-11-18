import sys
def validate_number(num):
    try:
        return float(num)
    except ValueError:
        return None


def process_data(numberA, numberB, numberC, numberD, numberE):
    numbers = [("A",numberA),("B",numberB),("C",numberC),("D",numberD),("E",numberE)]
    validated_numbers = []
    invalid_numbers = []
    negative_numbers = []

    for name, num in numbers:
        validated_num = validate_number(num)
        if validated_num is None:
            invalid_numbers.append(f"Number {name} with value '{num}' is not a valid number.")
        else:
            validated_numbers.append(validated_num)
            if validated_num < 0:
                negative_numbers.append(f"Number {name} with value: '{validated_num}' is negative.")

    if invalid_numbers:
        return f"""
        <p>Error: The following values are not valid numbers:</p>
        <ul>
            {"".join(f"<li>{error}</li>" for error in invalid_numbers)}
        </ul>
        """
    if any(num < 0 for num in validated_numbers):
        return f"""
        <p>Error: The following values are negative and are not allowed:</p>
        <ul>
            {"".join(f"<li>{error}</li>" for error in negative_numbers)}
        </ul>
        """
    count = len(validated_numbers)
    sum_numbers = sum(validated_numbers)
    avg = sum_numbers / count
    is_greater_than_50= sum_numbers > 50
    positive_count = sum(1 for num in validated_numbers if num > 0)

    avg_check = f"<p>The average ({avg}) is {'greater' if is_greater_than_50 else 'not greater'} than 50.</p>"
    count_check = f"<p>The count of positive numbers is {'even' if positive_count & 1 == 0 else 'odd'}.</p>"
    greater_than_10 = sorted(num for num in validated_numbers if num > 10)
    original_list = ", ".join(map(str, validated_numbers))
    sorted_list = ", ".join(map(str, greater_than_10))

    sorted_list_html = (
        f"<p>Sorted Values Greater Than 10: {sorted_list}</p>" if greater_than_10 
        else "<p>No values greater than 10 found.</p>"
    )

    output = f"""
            <p>Original Numbers: {original_list}</p>
            {sorted_list_html}
            {avg_check}
            {count_check}
    """
    return output

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("<p>Error: Please provide exactly five number arguments for a, b, c, d and e.</p>")
    else:
        numberA = sys.argv[1]
        numberB = sys.argv[2]
        numberC = sys.argv[3]
        numberD = sys.argv[4]
        numberE = sys.argv[5]

        print(process_data(numberA, numberB, numberC, numberD, numberE))
