import qualified Data.Map as M
import Data.List (find, sortBy)

main = do
    input <- readFile "Day7/input.txt"
    let commands = lines input
    let dirSizes = fst (fold commands)
    print $ M.foldl (+) 0 $ M.filter (<=100000) dirSizes
    let reqSpace = 30000000 - (70000000 - dirSizes M.! "/")
    print reqSpace
    let toDelete =  find (\a -> snd a > reqSpace) $ sortBy (\(_,a) (_,b) -> a `compare` b) $ M.toList dirSizes
    print toDelete

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