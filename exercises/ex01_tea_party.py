"""This exercise aims to help you plan a cozy tea party by asking for the number of guests, returning the amount of tea bags and treats needed as well as the cost for the whole thing."""

__author__: str = "730678627"


def main_planner(guests: int) -> None:
    """This function tells us the amount of teas, treats, and total cost of the tea party."""
    tea_count = tea_bags(people=guests)
    treat_count = treats(people=guests)
    total_cost = cost(tea_count=tea_count, treat_count=treat_count)
    print(f"A Cozy Tea Party for {guests} people!:")
    print(f"- Tea Bags: {tea_count}")
    print(f"- Treats: {treat_count}")
    print(f"- Cost: ${total_cost:.2f}")
    return None


def tea_bags(people: int) -> int:
    """This function describes the amount of tea bags needed per person."""
    return people * 2


def treats(people: int) -> int:
    """This function describes the amount of treats needed per person."""
    teas = tea_bags(people=people)
    treats_needed = teas * 1.5
    return int(treats_needed)


def cost(tea_count: int, treat_count: int) -> float:
    """This function describes how much the tea party will cost."""
    tea_bag_price = 0.5
    treat_price = 0.75
    total_cost = (tea_count * tea_bag_price) + (treat_count * treat_price)
    return total_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
