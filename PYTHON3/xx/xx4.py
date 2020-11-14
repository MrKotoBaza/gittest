import pygal
pie = pygal.Pie()
pie.title = "HelloWorld"
pie.add("Noname", 30)
pie.add("Set", 47)
pie.add("Rest", 23)

pie.render_in_browser()


    

