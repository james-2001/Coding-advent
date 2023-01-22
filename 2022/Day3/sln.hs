import Data.Char (ord)
import Data.List.Split (chunksOf)

main :: IO ()
main = do
    bag <- lines <$> readFile "Day3/input.txt"
    print $ sum $ map (scoreLetter . (head . findCommon) . splitInHalf) bag
    print $ sum $ map (scoreLetter . findCommon3Way) $ chunksOf 3 bag
splitInHalf :: [a] -> ([a], [a])
splitInHalf x = splitAt (length x `div` 2) x

findCommon :: ([Char], [Char]) -> [Char]
findCommon (a,b) =  filter (`elem` b ) a

scoreLetter :: Char -> Int
scoreLetter x
    | x `elem` ['a'..'z'] = ord x - 96
    | x `elem` ['A'..'Z'] = ord x - 38
    | otherwise = 0

findCommon3Way :: [[Char]] -> Char
findCommon3Way xs = head $ filter (\a -> a `elem` findCommon (head xs , xs !! 1)) (xs !! 2)