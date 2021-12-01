import Data.List.Split
import GHC.Show (Show)
import Data.Bits (xor)

main = do
    passwords <- readFile "input.txt"
    let splitLines = map (createField . words) $ lines passwords 
    let part1Count = length $ filter checkValid1 splitLines
    let part2Count = length $ filter checkValid2 splitLines
    print $ "Part 1: " ++ show part1Count
    print $ "Part 2: " ++ show part2Count

data PasswordField = PasswordField {range :: [Int],
                                    character :: Char,
                                    password :: String} deriving (Show)

createField :: [String] -> PasswordField
createField [a,b,c] = PasswordField {range = map (\s->read s ::Int) $ splitOn "-" a, character = head b, password = c}

countLetters :: String -> Char -> Int
countLetters str c = foldl (\acc char -> if char == c then acc+1 else acc) 0 str 

checkValid1 :: PasswordField -> Bool 
checkValid1 field = lower <= count && count <= upper 
                    where count = countLetters (password field) (character field)
                          lower = head $ range field 
                          upper = last $ range field

checkValid2 :: PasswordField -> Bool
checkValid2 PasswordField{range = a, character = c, password = p} = (lower == c) `xor` (upper == c)
                                                                     where lower = p !! (head a -1)
                                                                           upper = p !! (last a -1)