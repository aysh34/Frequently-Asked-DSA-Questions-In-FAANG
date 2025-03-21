class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        recipes = dict(zip(recipes, ingredients))
        made = []
        
     
        while True:
            new_recipe_made = False
            for rcp, igs in [*recipes.items()]:
                if not all(i in supplies for i in igs):
                    continue
                made.append(rcp)
                supplies.add(rcp)
                del recipes[rcp]
                new_recipe_made = True

            if not new_recipe_made: 
                break
        return made