import Data.List (isInfixOf)
import Data.Map (Map)
import Data.Graph (Graph, Vertex, graphFromEdges, graphFromEdges', transposeG, dfs)
import Data.List.Split
import Text.Read
import Data.Maybe (isNothing)
import GHC.Unicode (isDigit, isSpace)

main = do
    input <- readFile "test.txt"
    let sLines = map (removeWhiteSpace . splitOn "  " . removeNumbers . removeWordContaining "bag" . removeWordContaining "contain") $ splitOn "\n" input
    let (g, v, k) = graphFromEdges ([(head line, head line, tail line) | line <- sLines])
    let gT = transposeG g
    print $ v 3
    print $ length $ dfs gT [7] 

removeWordContaining:: String -> String -> String  
removeWordContaining target s = unwords $ map (\n -> if target `isInfixOf` n then "" else n ) $ words s

removeNumbers:: String -> String 
removeNumbers = filter (not. isDigit) 

pairList:: [String] -> [String]
pairList [] = []
pairList (x:y:xs) = (x++y): pairList xs

removeWhiteSpace:: [String] -> [String] 
removeWhiteSpace  = map $ filter $ not . isSpace  