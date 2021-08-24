import Data.List (isInfixOf)
import Data.Graph (graphFromEdges, transposeG, reachable)
import Data.List.Split
import Data.Maybe (fromMaybe)
import GHC.Unicode (isDigit, isSpace)

main = do
    input <- readFile "input.txt"
    let sLines = parseInput input
    let (g, _, k) = graphFromEdges ([(head line, head line, tail line) | line <- sLines])
    print $ length (reachable (transposeG g) (fromMaybe 0 $ k "shinygold")) -1
        

removeWordContaining:: String -> String -> String  
removeWordContaining target s = unwords $ map (\n -> if target `isInfixOf` n then "" else n ) $ words s

removeNumbers:: String -> String 
removeNumbers = filter (not. isDigit) 

removeWhiteSpace:: [String] -> [String] 
removeWhiteSpace  = map $ filter $ not . isSpace

parseInput:: String -> [[String]]
parseInput s = map (removeWhiteSpace . splitOn "  " . removeNumbers . removeWordContaining "bag" . removeWordContaining "contain") $ splitOn "\n" s