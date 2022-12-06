{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -w #-}
module Paths_x2022 (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where


import qualified Control.Exception as Exception
import qualified Data.List as List
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude


#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir `joinFileName` name)

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath



bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath
bindir     = "/home/james/Coding-advent/2022/.stack-work/install/x86_64-linux-tinfo6/72cbb3cdb8ac259b1324b16d90e7ccf3f6756c79b283e40ca928536bcfb3c5a8/9.2.5/bin"
libdir     = "/home/james/Coding-advent/2022/.stack-work/install/x86_64-linux-tinfo6/72cbb3cdb8ac259b1324b16d90e7ccf3f6756c79b283e40ca928536bcfb3c5a8/9.2.5/lib/x86_64-linux-ghc-9.2.5/x2022-0.1.0.0-7Qgp4xQOETXGez4Qv4tps4-x2022"
dynlibdir  = "/home/james/Coding-advent/2022/.stack-work/install/x86_64-linux-tinfo6/72cbb3cdb8ac259b1324b16d90e7ccf3f6756c79b283e40ca928536bcfb3c5a8/9.2.5/lib/x86_64-linux-ghc-9.2.5"
datadir    = "/home/james/Coding-advent/2022/.stack-work/install/x86_64-linux-tinfo6/72cbb3cdb8ac259b1324b16d90e7ccf3f6756c79b283e40ca928536bcfb3c5a8/9.2.5/share/x86_64-linux-ghc-9.2.5/x2022-0.1.0.0"
libexecdir = "/home/james/Coding-advent/2022/.stack-work/install/x86_64-linux-tinfo6/72cbb3cdb8ac259b1324b16d90e7ccf3f6756c79b283e40ca928536bcfb3c5a8/9.2.5/libexec/x86_64-linux-ghc-9.2.5/x2022-0.1.0.0"
sysconfdir = "/home/james/Coding-advent/2022/.stack-work/install/x86_64-linux-tinfo6/72cbb3cdb8ac259b1324b16d90e7ccf3f6756c79b283e40ca928536bcfb3c5a8/9.2.5/etc"

getBinDir     = catchIO (getEnv "x2022_bindir")     (\_ -> return bindir)
getLibDir     = catchIO (getEnv "x2022_libdir")     (\_ -> return libdir)
getDynLibDir  = catchIO (getEnv "x2022_dynlibdir")  (\_ -> return dynlibdir)
getDataDir    = catchIO (getEnv "x2022_datadir")    (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "x2022_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "x2022_sysconfdir") (\_ -> return sysconfdir)




joinFileName :: String -> String -> FilePath
joinFileName ""  fname = fname
joinFileName "." fname = fname
joinFileName dir ""    = dir
joinFileName dir fname
  | isPathSeparator (List.last dir) = dir ++ fname
  | otherwise                       = dir ++ pathSeparator : fname

pathSeparator :: Char
pathSeparator = '/'

isPathSeparator :: Char -> Bool
isPathSeparator c = c == '/'
