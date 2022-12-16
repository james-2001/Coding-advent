main :: IO ()
main = do 
    input <- readFile "Day10/input.txt"
    let all = findAccValues $ lines input
    let onesInScope =  filterCorrectVals all 
    print $ sum $ mapToSignalStrengths onesInScope

mapToSignalStrengths :: [(Int, Int)] -> [Int]
mapToSignalStrengths = map $ uncurry (*)

filterCorrectVals :: [(Int, Int)]-> [(Int, Int)]
filterCorrectVals = filter (\(_, cycle) -> cycle `elem` cycles)

cycles :: [Int]
cycles = take 6 [20 + 40*i | i <- [0..]]

findAccValues :: [String] -> [(Int, Int)]
findAccValues xs = concat $ scanl foldFn [(1,1)] xs

foldFn:: [(Int, Int)] -> String -> [(Int, Int)]
foldFn xs s 
    | "addx" `elem` s' = [(x, cycle + 1), (x + (read (last s') :: Int ), cycle + 2)]
    | "noop" `elem` s' = [(x, cycle + 1)]
    | otherwise = [(x, cycle)]
    where s' = words s
          (x, cycle) = last xs