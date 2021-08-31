import Data.Char (isSpace, isAlphaNum, digitToInt)

main = do
    input <- readFile "input.txt"
    let part1 = sum $ map evaluate $ lines input
    print part1


data Shunt = Shunt {operator::[Char], output:: [Char]} deriving(Show)

removeWhiteSpace:: String -> String 
removeWhiteSpace  = filter $ not . isSpace

evaluate:: String -> Int 
evaluate s = solveRPN $ shuntRPN $ foldl shuntFold (Shunt {operator ="", output =""}) $ removeWhiteSpace s

shuntFold:: Shunt -> Char -> Shunt
shuntFold acc x 
    | isAlphaNum x = Shunt {operator = operator acc, 
                            output = x:output acc}
    | x `elem` ['+', '*'] = Shunt {operator = x:dropWhile (/='(') (operator acc), 
                                   output = takeWhile (/='(') (operator acc) ++ output acc}
    | x== ')'= Shunt {operator = tail $ dropWhile (/='(') $ operator acc, 
                      output = takeWhile (/='(') (operator acc) ++ output acc}
    | x == '(' = Shunt {operator = x:operator acc, 
                        output = output acc}

shuntRPN:: Shunt -> String 
shuntRPN (Shunt {operator = op, output = ot}) = reverse $ op ++ ot

solveRPN:: String -> Int
solveRPN s = head $ foldl rpnFold [] s 
    where rpnFold (x:y:xs) '*' = (x * y):xs
          rpnFold (x:y:xs) '+' = (x + y):xs
          rpnFold xs n = digitToInt n:xs