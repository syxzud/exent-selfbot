import holder
import globals
import random

exent = holder.bot

@exent.command()
async def mines(ctx, horizontal: int, vertical: int, mines: int):
    await ctx.message.delete()
    # Create a grid initialized with zero emojis
    grid = [['||0️⃣||' for _ in range(horizontal)] for _ in range(vertical)]
    
    # Randomly place mines
    mine_positions = set()
    while len(mine_positions) < mines:
        x = random.randint(0, horizontal - 1)
        y = random.randint(0, vertical - 1)
        mine_positions.add((x, y))
    
    for (x, y) in mine_positions:
        grid[y][x] = '||💥||'
    
    # Convert grid to a string for sending
    grid_str = '\n'.join([''.join(row) for row in grid])
    
    await ctx.send(grid_str)
