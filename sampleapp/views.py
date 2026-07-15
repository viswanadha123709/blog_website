from django.shortcuts import render

items = {
    "popcorn": 0,
    "cookies": 0,
    "donut": 0,
    "chocolate": 0,
    "candy": 0,
    "peanuts": 0,
    "softdrink": 0,
    "fruitjuice": 0,
    "apple": 0,
    "banana": 0,
    "cupcake": 0,
    "cake": 0
}

prices = {
    "popcorn": 20,
    "cookies": 25,
    "donut": 30,
    "chocolate": 40,
    "candy": 10,
    "peanuts": 20,
    "softdrink": 30,
    "fruitjuice": 35,
    "apple": 25,
    "banana": 15,
    "cupcake": 35,
    "cake": 50
}
def demo(request):

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "clear":

            for i in items:
                items[i] = 0

        elif action == "bill":

            # Bill generation code
            pass

        else:

            item, operation = action.split()

            if operation == "add":
                items[item] += 1

            elif operation == "sub":
                if items[item] > 0:
                    items[item] -= 1

    total = 0

    for item in prices:
        total += items[item] * prices[item]

    context = items.copy()
    context["total"] = total

    return render(request, "first.html")