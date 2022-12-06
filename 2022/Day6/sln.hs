import Data.Set (fromList, toList)
import Data.List.Split (chunksOf)

main = do
    input <- readFile "Day6/input.txt" 
    print $ map (\a -> (+) a $ length $ takeWhile checkForDuplicates $ getChunks a input) [4, 14]

checkForDuplicates :: Ord a => [a] -> Bool
checkForDuplicates xs = length (mkUnique xs) /= length xs

mkUnique ::Ord a => [a] -> [a]
mkUnique = toList . fromList 

getChunks :: Int -> [a] -> [[a]]
getChunks n xs = filter (\a -> length a == n ) $ splitInput n xs

splitInput :: Int -> [a] -> [[a]]
splitInput n [] = []
splitInput n xs = c : splitInput n (tail  xs) where c = take n xs 
