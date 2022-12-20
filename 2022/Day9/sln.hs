import Data.List (nub)
main = do 
    input <- readFile "Day9/input.txt"
    let cmds = concatMap (parseLine . words) $ lines  input
    let positions = foldl foldFn ([0,0], [0,0], [[0,0]]) cmds
    print $ length $ nub $ thrd positions
    let ropePos = foldl foldFn2 (replicate 10 [0,0], [[0,0]]) cmds
    -- print ropePos
    print $ length $ nub $ snd ropePos


parseLine:: [[Char]] -> [[Int]]
parseLine [dir,v]
    | dir == "R" = replicate i [0,1]
    | dir == "U" = replicate i [1,0]
    | dir == "L" = replicate i [0,-1]
    | dir == "D" = replicate i [-1,0]
    | otherwise = [[0,0]]
    where i = read v:: Int
parseLine xs = [[0,0]]

thrd :: (a,b,c) -> c
thrd (_,_,a) = a  

foldFn:: ([Int], [Int], [[Int]]) -> [Int] -> ([Int], [Int], [[Int]])
foldFn (h, t, visited) x = (newHead, follow newHead t , (follow newHead t):visited) where newHead = move h x

foldFn2 :: ([[Int]], [[Int]]) -> [Int] -> ([[Int]], [[Int]])
foldFn2 (h:rope, visited) x = (newRope, last newRope:visited) where newRope = scanl follow (move h x) rope  
foldFn2 _ _ = ([[123]], [[456]])

move :: [Int] -> [Int] -> [Int]
move = zipWith (+)

follow :: [Int] -> [Int] -> [Int]
follow h t
    | h `isAdj` t = t
    | otherwise = zipWith (+) (map getSign off) t where off = zipWith (-) h t

isAdj:: [Int] -> [Int] -> Bool
isAdj h t = all (\x -> abs x <=1) (zipWith (-) h t)

getSign:: Int -> Int
getSign 0 = 0
getSign x = x `div` abs x