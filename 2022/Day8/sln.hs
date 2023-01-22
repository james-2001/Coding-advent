import Data.Char (digitToInt)
import Data.List (reverse, transpose, zipWith4, product, maximum)

main = do
    trees <- parseHorizontal <$> readFile "Day8/input.txt"
    print $ countVisible $ zipAngles $ map (concat . getVisibleOfRotation trees) [0..3]
    print $ maximum $ findViewingDistances $ getAllVisibleLengths trees

countVisible :: [[Bool]] -> Int
countVisible xs = length $ filter id $ map or xs

zipAngles :: [[a]] -> [[a]]
zipAngles [a,b,c,d] = zipWith4 (\i j k l -> [i,j,k,l]) a b c d
zipAngles _ = []

pointMax :: [Int] -> [Int]
pointMax = tail . scanl max 0

isVisible :: [Int] -> [Bool]
isVisible xs = init $ zipWith (>) (xs++[0]) (-1:pointMax xs)

parseHorizontal :: [Char] -> [[Int]]
parseHorizontal trees = map (map digitToInt) $ lines trees

rotate :: [[a]] -> [[a]]
rotate = reverse . transpose 

unrotate :: [[a]] -> [[a]]
unrotate = transpose . reverse

rotateN :: [[a]] -> Int -> [[a]]
rotateN xs n = iterate rotate xs !! n

unrotateN :: [[a]] -> Int ->[[a]]
unrotateN xs n = iterate unrotate xs !! n

getVisibleOfRotation :: [[Int]] -> Int -> [[Bool]]
getVisibleOfRotation xs n = unrotateN ( map isVisible (rotateN xs n)) n

viewLength :: [Int] -> Int
viewLength [] = 0
viewLength (x:xs) = length (takeWhileInc (<x) xs)

takeWhileInc :: (a -> Bool) -> [a] -> [a]
takeWhileInc f xs = case zs of [] -> ys
                               (z:_) -> ys ++ [z]
                    where (ys, zs) = span f xs
findVisibleLength :: [Int] -> [Int]
findVisibleLength [] = []
findVisibleLength (x:xs) = viewLength (x:xs) : findVisibleLength xs

findVisibleLengthOfRotation :: [[Int]] -> Int -> [Int]
findVisibleLengthOfRotation xs n = concat $ unrotateN (map findVisibleLength (rotateN xs n)) n

getAllVisibleLengths :: [[Int]] -> [[Int]]
getAllVisibleLengths xs = zipAngles $ map (findVisibleLengthOfRotation xs ) [0..3]

findViewingDistances :: [[Int]] -> [Int]
findViewingDistances = map product