#Graph/Map Colouring Problem
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
states = ['Andhra', 'Karnataka', 'TamilNadu', 'Kerala']

neighbors = {}
neighbors['Andhra'] = ['Karnataka', 'TamilNadu']
neighbors['Karnataka'] = ['Andhra', 'TamilNadu', 'Kerala']
neighbors['TamilNadu'] = ['Andhra', 'Karnataka', 'Kerala']
neighbors['Kerala'] = ['Karnataka', 'TamilNadu']

colors_of_states = {}

def promising(s, c):
    for n in neighbors.get(s):
        neighbor_color = colors_of_states.get(n)
        if neighbor_color == c:
            return False
    return True

def get_color_for_state(s):
    for c in colors:
        if promising(s, c):
            return color

def main():
    for s in states:
        colors_of_states[s] = get_color_for_state(s)
    print (colors_of_states)

main()