main = do 
    input <- readFile "Day2/input.txt"
    print $ sum $ map (scorePart2 . replacePair. words) $ lines input
    

replaceLetter :: Num p => [Char] -> p
replaceLetter a
    | a `elem` ["A", "X"] = 0
    | a `elem` ["B", "Y"] = 1
    | a `elem` ["C", "Z"] = 2
    | otherwise = 0

replacePair :: [[Char]] -> [Integer]
replacePair = map replaceLetter

scorePart1 :: Integral a => [a] -> a
scorePart1 [a,b]
    | a == b = 3 + b + 1
    | (b+1) `mod` 3 == a = b + 1
    | otherwise = 6 + b + 1
scorePart1 _ = 0

scorePart2 :: Integral a => [a] -> a
scorePart2 [a,b]
    | b == 0 =  1 + ( (a-1) `mod` 3)
    | b == 1 = 3 + a + 1
    | b == 2 = 6 + ((a+1) `mod` 3) + 1 
scorePart2 _ = 0