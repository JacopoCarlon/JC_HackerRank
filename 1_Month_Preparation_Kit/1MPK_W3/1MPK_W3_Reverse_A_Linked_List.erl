-module(solution).
-export([main/0]).
-import(os, [getenv/1]).

-record(singlyLinkedListNode, {data, next}).

create_singly_linked_list([]) ->
    null;
create_singly_linked_list([H | T]) ->
    #singlyLinkedListNode{data = H, next = create_singly_linked_list(T)}.

print_singly_linked_list(L) ->
    print_singly_linked_list(L, []).

print_singly_linked_list(null, Acc) ->
    Acc;
print_singly_linked_list(L, Acc) ->
    print_singly_linked_list(L#singlyLinkedListNode.next, Acc ++ [L#singlyLinkedListNode.data]).

%
% Complete the 'reverse' function below.
%
% The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
% The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
%

%
% For your reference:
%
% singlyLinkedListNode = {
%     data = int,
%     next = singlyLinkedListNode
% }
%
%

reverse(Llist) ->
    % Write your code here
    reverse(Llist, null).
    
reverse(null, Acc) -> Acc;
reverse(Node, Acc) ->
    NewAcc = #singlyLinkedListNode{data = Node#singlyLinkedListNode.data, next = Acc},
    reverse(Node#singlyLinkedListNode.next, NewAcc).

read_multiple_lines_as_list_of_strings(N) ->
    read_multiple_lines_as_list_of_strings(N, []).

read_multiple_lines_as_list_of_strings(0, Acc) ->
    lists:reverse(Acc);
read_multiple_lines_as_list_of_strings(N, Acc) when N > 0 ->
    read_multiple_lines_as_list_of_strings(N - 1, [string:chomp(io:get_line("")) | Acc]).

main() ->
    {ok, Fptr} = file:open(getenv("OUTPUT_PATH"), [write]),

    {Tests, _} = string:to_integer(string:chomp(io:get_line(""))),

    lists:foreach(fun(TestsItr) ->
        {LlistTempCount, _} = string:to_integer(string:chomp(io:get_line(""))),

        LlistTempTemp = read_multiple_lines_as_list_of_strings(LlistTempCount),

        LlistTemp = lists:map(fun(X) -> {I, _} = string:to_integer(X), I end, LlistTempTemp),

        Llist = create_singly_linked_list(LlistTemp),

        Llist1 = reverse(Llist),

        Llist1Traversal = print_singly_linked_list(Llist1),

        io:fwrite(Fptr, "~s~n", [lists:join(" ", lists:map(fun(X) -> integer_to_list(X) end, Llist1Traversal))]) end,
    lists:seq(1, Tests)),

    file:close(Fptr),

    ok.
