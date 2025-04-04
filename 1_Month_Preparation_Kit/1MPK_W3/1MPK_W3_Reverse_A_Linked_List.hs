{-# LANGUAGE FlexibleInstances, UndecidableInstances, DuplicateRecordFields #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.List
import Data.List.Split
import Data.Set
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

data SinglyLinkedListNode = SinglyLinkedListNode {
    nodeData :: Int,
    next :: SinglyLinkedListNode
} | SinglyLinkedListNodeNil

createSinglyLinkedList :: [Int] -> SinglyLinkedListNode
createSinglyLinkedList [] = SinglyLinkedListNodeNil
createSinglyLinkedList (x:xs) = SinglyLinkedListNode {
    nodeData = x,
    next = createSinglyLinkedList xs
}

instance {-# OVERLAPPING #-} Show (SinglyLinkedListNode, String) where
    show (SinglyLinkedListNodeNil, _) = ""
    show (SinglyLinkedListNode x SinglyLinkedListNodeNil, _) = show x
    show (SinglyLinkedListNode x xs, sep) = show x ++ sep ++ show(xs, sep)

--
-- Complete the 'reverse' function below.
--
-- The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
-- The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
--

--
-- For your reference:
--
-- SinglyLinkedListNode {
--     nodeData :: Int
--     next :: SinglyLinkedListNode
-- }
--
--


-- function is pure and requires no do
-- reverse llist = do
--    -- Write your code here


reverse :: SinglyLinkedListNode -> SinglyLinkedListNode
reverse llist = reverseHelper llist SinglyLinkedListNodeNil
    where
        reverseHelper SinglyLinkedListNodeNil acc = acc
        reverseHelper (SinglyLinkedListNode x next) acc = 
            reverseHelper next (SinglyLinkedListNode x acc)


readMultipleLinesAsStringArray :: Int -> IO [String]
readMultipleLinesAsStringArray 0 = return []
readMultipleLinesAsStringArray n = do
    line <- getLine
    rest <- readMultipleLinesAsStringArray(n - 1)
    return (line : rest)

main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    tests <- readLn :: IO Int

    forM_ [1..tests] $ \tests_itr -> do
        llistTempCount <- readLn :: IO Int

        llistTempTemp <- readMultipleLinesAsStringArray llistTempCount
        let llistTemp = Data.List.map (read :: String -> Int) llistTempTemp

        let llist = createSinglyLinkedList llistTemp

        let llist1 = reverse llist

        hPutStrLn fptr $ show(llist1, " ")

    hFlush fptr
    hClose fptr
