import AI_functs
import game_logic
import Main_Decision_Tree


def AI_wild_pick_4(board, deck, player, target, selected_color):
    """
    Card function that handles when the player plays a wild pick 4 card.
    """
    board.color = selected_color
    print("New color: ", board.color)
    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 4)
    print("Trageted players hand size after: ", len(target.hand))


def AI_wild_color(board, player, selected_color):
    """
    Card function that handles when the player plays a wild color card.
    """
    board.color = selected_color
    print("New color: ", board.color)


def AI_draw_2(deck, player, target):
    """
    Card function that handles when the player plays a draw 2 card.
    """
    print("Targeted player: ", target.name)
    print("Trageted players hand size before: ", len(target.hand))
    target.grab_cards(deck, 2)
    print("Trageted players hand size after: ", len(target.hand))


def AI_skip(board, player, target):
    """
    Card function that handles when the player plays a skip turn card.
    """
    print("Targeted player skipping: ", target.name)
    target.skip = True

#TODO
def reverse(board):
    """
    Card function that handles when the player plays the reverse card.

    Prints the original turn_iterator and then swaps sign of the
    original turn_iterator.

    Args: board class of a pyuno game in which its turn_iterator value will be
    accessed (should be 1 or -1)
    """
    turn_iterator = board.turn_iterator
    print("reversing", turn_iterator)
    board.turn_iterator = -turn_iterator

########################################################


def AI_card_played_type(board, deck, player, players, target=None, selected_color=None):
    """
    Logic function that takes the most recently played card and decides
    what game actions are needed to be taken to accomadate. These actions are
    then preformed by other functions detailed above.
    """

    # check to see if AI won
    if player.hand == []:
        game_logic.add_winner(player)

    # if no target was selected set target to be most hated player
    if target is None:
        (max_hate, hate_player) = AI_functs.fetch_hate_priority(player, players)
        target = hate_player

    # if no color was selected set it to most common_color
    if selected_color is None:
        selected_color = AI_functs.fetch_most_common_color(player)

    played_type = board.type
    played_color = board.color

    print("played by: ", player.name)
    print("played card type: ", played_type)
    print("played card color: ", played_color)

    if played_color == "w":
        if played_type == "d":      # wild choose color draw 4 card played
            AI_wild_pick_4(board, deck, player, target, selected_color)
        elif played_type == "c":    # wild choose color card played
            AI_wild_color(board, deck, selected_color)

        # go through Main_Decision_Tree as another card can be played
        # as the AI played a wild card
        if player.hand == []: # catch if the player has won
            return
        else:
            print("wild card played, playing again.")
            Main_Decision_Tree.travel_Main_Decision_Tree(board, deck, player,
                                                         players, player.Main_Decision_Tree.Dec_Tree)

    elif played_type == "p":        # draw 2 card played
        AI_draw_2(deck, player, target)

    elif played_type == "s":        # skip turn card played
        AI_skip(board, player, target)

    elif played_type == "r":     # TODO TODO SPECIAL WORK NEEDED
        reverse(board)
    elif played_type.isdigit():     # normal number card played
        pass
