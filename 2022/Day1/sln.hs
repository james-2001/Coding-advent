import Data.List.Split
import Data.List

main = do 
    calories <- readFile "Day1/input.txt"
    print $ map (takeMax calories) [1,3]

parseToInt = map (\y -> read y :: Integer) 

takeMax x n = sum $ take n $ reverse $ sort $ map (sum . parseToInt) $ splitWhen (=="") $ lines x