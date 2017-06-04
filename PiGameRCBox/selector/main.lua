require "lpeg"

love.window.setTitle( "Selection Screen" )
W, H = 1000, 800
love.window.setMode(W, H)

games = {}
thumbnail_size = 360
padding = 10

function parse_games_test()
  local equalcount = lpeg.P{
    "S";   -- initial rule name
    S = "a" * lpeg.V"B" + "b" * lpeg.V"A" + "",
    A = "a" * lpeg.V"S" + "b" * lpeg.V"A" * lpeg.V"A",
    B = "b" * lpeg.V"S" + "a" * lpeg.V"B" * lpeg.V"B",
  } * -1
  print(lpeg.match(equalcount, ""))
end

function parse_games()

  -- rewrite to handle JSON files like:
  -- {
	-- "path": "main.lua",
	-- "engine": "Love2D",
	-- "keyboard": "required",
	-- "mouse": "not supported",
	-- "gamepad": "not supported",
	-- "network": "not supported",
	-- "multiplayer": "none",
	-- "singleplayer": "true",
  --
  -- "title": "game title", TODO add to PR
	-- "author": "ur name",
	-- "batch": "ur batch",
	-- "website": "http://github.com/jfkfjfkfj",
	-- "splash": "rcgc/splash.png",
	-- "screenshot": "rcgc/screenshot.png"
  -- }

  local cx, cy = padding, padding
  for game in io.popen([[dir "C:\rc_misc\PiGameRCBox\selector\games" /b]]):lines() do
    print(game)
    i = love.graphics.newImage( "games/" .. game )
    title = string.match(game, "([^.]+)%.")
    games[title] = {thumbnail = i, x = cx, y = cy}
    cx = cx + thumbnail_size + padding
    if cx > W - thumbnail_size then
      cx = padding
      cy = cy + thumbnail_size + padding*2
    end
  end
end

function love.load()
  parse_games()
  parse_games_test()
end

function love.draw()
  for title, game in pairs(games) do
    love.graphics.draw(game.thumbnail, game.x, game.y)
    love.graphics.printf(title, game.x, game.y+thumbnail_size, thumbnail_size, "center")
  end
end

function love.update(dt)
end

function love.mousereleased(x, y)
  for title, game in pairs(games) do
    if x > game.x and x < game.x + thumbnail_size and y > game.y and y < game.y + thumbnail_size then
      print("clicked on " .. title)
    end
  end
end
