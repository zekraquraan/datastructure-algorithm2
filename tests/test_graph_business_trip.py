from graph_business_trip.graph_business_trip import Graph, business_trip


def test_business_trip():
    graph = Graph()
    
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_edge("Pandora", "Arendelle", 150)
    
    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    graph.add_vertex("Narnia")
    graph.add_edge("Arendelle", "New Monstropolis", 42)
    graph.add_edge("New Monstropolis", "Naboo", 73)
    graph.add_edge("Naboo", "Narnia", 250)
    
    graph.add_vertex("Naboo")
    graph.add_vertex("Metroville")
    graph.add_edge("Naboo", "Metroville", 26)
    
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Metroville")
    graph.add_vertex("Narnia")
    graph.add_edge("New Monstropolis", "Metroville", 105)
    graph.add_edge("Arendelle", "Metroville", 99)
    graph.add_edge("Metroville", "Narnia", 37)
    
    city_names = ["Metroville", "Pandora"]
    cost = business_trip(graph, city_names)
    assert cost == 82

def test_case_1():
    graph = Graph()
    
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_edge("Pandora", "Arendelle", 150)
    
    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    graph.add_vertex("Narnia")
    graph.add_edge("Arendelle", "New Monstropolis", 42)
    graph.add_edge("New Monstropolis", "Naboo", 73)
    graph.add_edge("Naboo", "Narnia", 250)
    
    graph.add_vertex("Naboo")
    graph.add_vertex("Metroville")
    graph.add_edge("Naboo", "Metroville", 26)
    
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Metroville")
    graph.add_vertex("Narnia")
    graph.add_edge("New Monstropolis", "Metroville", 105)
    graph.add_edge("Arendelle", "Metroville", 99)
    graph.add_edge("Metroville", "Narnia", 37)

    city_names = ['Arendelle', 'New Monstropolis', 'Naboo']
    cost = business_trip(graph, city_names)
    assert cost == 115

def test_case_2():
    graph = Graph()
    
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_edge("Pandora", "Arendelle", 150)
    
    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    graph.add_vertex("Narnia")
    graph.add_edge("Arendelle", "New Monstropolis", 42)
    graph.add_edge("New Monstropolis", "Naboo", 73)
    graph.add_edge("Naboo", "Narnia", 250)
    
    graph.add_vertex("Naboo")
    graph.add_vertex("Metroville")
    graph.add_edge("Naboo", "Metroville", 26)
    
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Metroville")
    graph.add_vertex("Narnia")
    graph.add_edge("New Monstropolis", "Metroville", 105)
    graph.add_edge("Arendelle", "Metroville", 99)
    graph.add_edge("Metroville", "Narnia", 37)

    city_names = ['Naboo', 'Pandora']
    cost = business_trip(graph, city_names)
    assert cost is None

def test_case_3():
    graph = Graph()
    
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_edge("Pandora", "Arendelle", 150)
    
    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    graph.add_vertex("Narnia")
    graph.add_edge("Arendelle", "New Monstropolis", 42)
    graph.add_edge("New Monstropolis", "Naboo", 73)
    graph.add_edge("Naboo", "Narnia", 250)
    
    graph.add_vertex("Naboo")
    graph.add_vertex("Metroville")
    graph.add_edge("Naboo", "Metroville", 26)
    
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Metroville")
    graph.add_vertex("Narnia")
    graph.add_edge("New Monstropolis", "Metroville", 105)
    graph.add_edge("Arendelle", "Metroville", 99)
    graph.add_edge("Metroville", "Narnia", 37)

    city_names = ['Narnia', 'Arendelle', 'Naboo']
    cost = business_trip(graph, city_names)
    assert cost is None
