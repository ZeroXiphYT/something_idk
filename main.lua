local col = require 'ansicolors'

--Functions
function Lose()
    print(col('%{red} YOU DIED!, you have to restart if you want to play again'))

end
function PlayGame()
    io.write("Ok, First Challenge, Is Lua Similiar To Python(y or n)\n")
    Ans1 = io.read()
    if Ans1 == "y"
    then
       Question2() 
       else
        Lose()
    end
end

function Question2()
io.write(col("%{green}Well Done").." Now For The Second Question, Does Lua Have Indentation Rules Like Python(y or n)\n")
Ans2 = io.read()
if Ans2 == "n"
    then
        Question3()
    else
        Lose()
    end
end
function Question3()
io.write(col("%{green} Very Good Job").." Now For The Last Question, Is Lua mainly used for games?(y or n)\n")
Ans3 = io.read()
if Ans3 == "y"
then
    Win()
    else
        Lose()
end
end
function Win()
print(col('%{cyan} YOU WON $1,000,000!!!!!!!, YOU WON THE GAME!!!!'))
end


--Start Stuff
io.write("Welcome Player, What Should I Call You?\n")
PlayerName = io.read()
io.write(col('%{cyan} Hello '..PlayerName.."\n"))
io.write("There Will Be 3 Challenges, If You Beat All Of Them You Win, but if lose any you"..col('%{red} DIE!\n'))
io.write("Do you accept (y or n)\n")
Play = io.read()
if Play == "y"
then
    PlayGame()
else
    io.write("Play Whenever You Want "..PlayerName)
end