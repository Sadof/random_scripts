class person:
    def __init__(self, name , job = None , interests = None):
        self.name = name
        self.job = job
        self.interests = interests
    def change_name(self, new_name):
        self.name = new_name
    def __str__(self):
        return ' Person: %s\n Job: %s\n Interests: %s' % (self.name, self.job, self.interests)


i = person("Maxib U")
i.job = ('idk')
i.interests = 'anime, games'
print(i)
i.change_name('1 2')
print(i)
