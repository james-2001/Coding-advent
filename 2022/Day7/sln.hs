import Data.List.Split (splitOn)
newtype Folder = Folder ([Folder], [File]) deriving (Show) 
data File = File [Char] Int deriving (Show)

main = do
    input <- readFile "Day7/test.txt"
    let splitInput = splitOn "$ ls" input
    print $ map lines splitInput
