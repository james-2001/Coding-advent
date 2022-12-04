import Data.List.Split (splitOn)
import Data.List (intersect)

main = do
    input <- readFile "Day4/input.txt"
    print $ length $ filter id $ map (checkAreas . splitOn ",") $ lines input
    print $ length $ filter id $ map (checkAreas2 . splitOn ",") $ lines input

convertToRange :: [Char] -> [Integer]
convertToRange x = [read a :: Integer .. read b :: Integer] 
                    where [a,b] = splitOn "-" x

checkAreas :: [[Char]] -> Bool
checkAreas xs =  (a' `intersect` b') `elem` [a',b']  where [a',b'] = map convertToRange xs

checkAreas2 :: [[Char]] -> Bool
checkAreas2 xs =  (a' `intersect` b') /= []  where [a',b'] = map convertToRange xs