love.window.setTitle( "Selection Screen" )


function love.load()
   for dir in io.popen([[dir "C:\rc_misc\PiGameRCBox\selector\games" /b]]):lines() do print(dir) end
end

function love.draw()
end

function love.update(dt)
end

function love.mousemoved(mx, my)
end
