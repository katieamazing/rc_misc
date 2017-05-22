love.window.setTitle( "Selection Screen" )
W, H = 1000, 800
love.window.setMode(W, H)

games = {}
thumbnail_size = 360
padding = 10

function love.load()
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
