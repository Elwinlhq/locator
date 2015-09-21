%%====================================================================
%%
%% @author Juanse Perez Herrero <juanseph@gmail.com> [http://bytefilia.com]
%% @copyright CC Attribution - 2013
%%
%% Dummy runner module
%%
%%====================================================================
-module(console).
-export([run/0]).

%% run the gen_server server_template
run() -> 
    server_template:start([1,2,3]),
    gen_server:cast(server_template, {do_something, "Parameter"}),
    gen_server:call(server_template, {do_something, "Parameter2"}),	
    server_template:stop().
        
