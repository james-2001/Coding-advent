import qualified Data.Map as M
import Data.List (find, sortBy)

main = do
    dirSizes <- fst . fold . lines <$> readFile "Day7/input.txt"
    print $ M.foldl (+) 0 $ M.filter (<=100000) dirSizes
    print $ snd <$> find (\a -> snd a > reqSpace' dirSizes) (sortBy compareTupleBySecond $ M.toList dirSizes)

compareTupleBySecond :: Ord a1 => (a2, a1) -> (a3, a1) -> Ordering
compareTupleBySecond (_,a) (_,b) = a `compare` b  

reqSpace':: M.Map [Char] Int -> Int
reqSpace' m = 30000000 - (70000000 - m M.! "/")

fold :: [[Char]] -> (M.Map [Char] Int, [String])
fold = foldl processIns (M.singleton "/" 0, ["/"]) 

processIns:: (M.Map [Char] Int, [String]) -> [Char] -> (M.Map [Char] Int, [String])
processIns (m,x) s 
    | a == "$" &&  b == "cd" && c == "/" = (m,["/"])
    | a == "$" &&  b == "cd" && c == ".." = (m, tail x)
    | a == "$" &&  b == "cd" = (m, (head x ++ c):x)
    | "ls" `elem` s' = (m,x)
    | a == "dir" = (m,x) 
    | otherwise = (addtoAllInPwd m x size, x)
    where s' = words s
          a:b:xs = s'
          c = head xs
          size = read a :: Int

addtoAllInPwd:: M.Map [Char] Int -> [String] -> Int -> M.Map [Char] Int
addtoAllInPwd m pwd size = foldl (\acc s -> M.insertWith (+) s size acc ) m pwd