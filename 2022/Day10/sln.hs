main = do 
    input <- readFile "Day10/test.txt"
    print $ applyToPointer $ mapToFns $ lines input

applyToPointer:: [Int -> Int] -> Int
applyToPointer = foldl (\acc f -> f acc) 0

mapToFns:: [[Char]] -> [Int -> Int]
mapToFns = map swapForFn

swapForFn :: [Char] -> (Int -> Int)
swapForFn s 
    | "addx" `elem` s' = (+ (read (last s') :: Int ))
    | "noop" `elem` s' = id
    | otherwise = id
    where s' = words s