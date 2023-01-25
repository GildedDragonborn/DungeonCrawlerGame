# DungeonCrawlerGame
A small dungeon crawler I am working on

12/9/22 - rebased code, any prior commits will show as having been done today. Commits ranged since 10/28/22 to 12/8/22

1/4/23 - Happy new year, updated todo list to reflect tasks still in need of completion.

TODO:
>### Things I can do on my own
> - Rewrite level generation to include room variant and hostile attributes (turn int into list [id, 'variant', T/F])
>   - ~~Start with pre-generated level~~
> - Minimap
> - Add enemies and behaviors:
>   - Sprites for different enemies
>   - Boss Sprite
>   - Mini-Boss Sprite
>   - ~~Stationary Behavior~~
>   - Pursuer Behavior
>     - NOTE: DEBUG AND MAKE ENEMIES NOT ABLE TO COLLIDE OR BE ON SAME SPACE
>   - Patroller Behavior
>   - Random Behavior
>   - Mini-Boss Behavior
>   - Boss Behavior
> - Add enemies to rooms (have to do by hand, pain)
>   - PROGRESS UPDATE: SOME ENEMIES ADDED, ADD MORE
> - Refine Level Generation
>   - IDEAS:
>     - Find a better vertical weight than 2
>     - Have one set Starting point for the crawler
>     - Completely rewrite the crawler (*pain*)
>   - Fix randomly spawning in boss room
> - Battle Scenes
>   - ~~Battle scene trigger~~
>   - Basic menu interaction
>   - Combat System
>   - Flee mechanic(?)
>   - Enemy Encounters
>   - Boss Fights
> - Implement Leveling System
>   - Leave level - keep gold, lose XP
>   - Die in level - keep XP, lose gold
>   - Spend XP to level up
>   - *Death as a mechanic*
> - Implement hub area for player to load into the game in
>   - Store to buy equipment/consumables
>   - Blacksmith to improve equipment
>   - NPCs to fill out story
> - Placeholder textures for enemies, NPCs, and other
>   - NCSs:
>     - Shopkeeper
>     - Generic Townsfolk (maybe 6 or 7 different ones?)
>   - Enemies:
>     - ~~Cultist~~
>     - ~~Skeleton~~
>     - Cult Leader *insert name* (boss)
>     - Aberration from beyond (rare alt-boss)
>     - ~~Failed Summon (miniboss)~~
>   - Other:
>     - Shop
>     - Hub Area
>     - Shop (in dungeon)
> - Make a list of all weapons and armor a player can have
>   - THEN implement said list in BaseWeapons.json and BaseArmor.json
> - Make Character origins (different starting characters) 
> - Add menus for leveling up, purchasing, and entering the manor
> - Minimap for rooms explored
> - List of perks and what they do
> - ~~Fix trapdoor being funky~~
> - (optional) Consumable items
>   - Start by making a list of potential items and effects
>   - Implement easier ones, then wait until first play-tests to add more
> - Design level variations
>   - room variations a-e for all
> - Storyboarding
>   - *Likely to be last step*
>   - NPCs and their histories
>   - PC and why they continue to delve into the manor
>     - *All character origins are same character, different timeline*
>   - *LORE?*


>   
> ### Things I cannot do on my own 
>  - Texture Updates 
>   - Replace character sprite
>   - Replace Floor Textures
>   - Replace Wall Textures
>  - Music + Sound Effects
>  - Animations for player and enemies
>    - Player movement
>      - up 
>      - down
>      - left
>      - right
>      - into doors
>      - obstacle block path
>      - battle animations
>        - Sword swing
>        - Axe Swing
>        - Gun(?)
>        - Take Damage
>        - Death
>        - Victory
>    - Enemy Movement
>      - up 
>      - down
>      - left
>      - right
>      - Battle animations
>        - Attack (Spell cast + generic attack for each)
>        - Take Damage
>        - Death
>        - Victory
>    - Boss Animations
>      - Animation of entering boss room and alt version of the summoned horror