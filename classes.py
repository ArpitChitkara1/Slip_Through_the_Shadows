class game_map:
    # made a class game_map in which everything is done.

    # assigned the moves to a variable and names it move_list.
    moves_list = "U" \
                 or "D" \
                 or "L" \
                 or "R"


    def __init__(self, map_file, guard_file):
        self.guard_file_name = str(guard_file)
        self.map_file_name = str(map_file)
        self.row_1 = 0
        self.col_1 = 0
        self.win_point = 0
        # saying that I want to ensure that guard_file is taken as a string and also  map_file is string.

        try:
            # using try function to make sure there are no errors in future and I get to know where the error is.
            map_read = open(map_file)
            # opening the file
            map_display = map_read.read()
            # reading the file and assigning it to a variable.
            map_read.close()
            # closing the map.

            reading_map = open(map_file)
            # reading line in the map again because now I want just lines to be read.
            display_map = reading_map.readlines()
            # giving the val of display_map to self.
            self.display_map = display_map

            # making an extra list  which is empty for now and then appending data to it.

            data_list_to_append = []
            for item in display_map:
                # Using len function to check if the item is in the range of length of the map file and then using them further.
                strip_list = []
                # checking for spaces in the read lines and then removing them.
                for blank in item.rstrip():
                    # making a strip list in which all the stripped items will be put.
                    strip_list.append(blank)
                    # appending the blank list to the list
                data_list_to_append.append(strip_list)
                # appending the list to my main list
                # telling that var is  string


                # if the item is = 11 then it is in the end, and then we don't need to pop anything.

                # Using pop function to remove the blank space in list which has the data and then the indexes change for all.

                # appending the var to the list which is the guard_list in actual.

            self.data_list_to_append = data_list_to_append
            # giving the value od list to self.

            # closing the  file.
            map_read.close()
        except Exception as m:
            # giving exception to know if this part of the code didn't work
            print(m)
        try:
            # opening the guard_file again for getting the indexes and appending them to other list then.
            read_guard = open(guard_file)
            display_guard = read_guard.readlines()
            # reading the lines just like I did  earlier.
            self.display_guard = display_guard
            # giving the values to Self.

            self.data_guards = []
            # making an empty list for now.

            # using a for loop for knowing if the item is in the display_guard which is a variable that read the lines.

            for item in display_guard:
                # splitting the file so that I can get each item separately because they are in different lines.
                file_guard = item.split()

                self.data_guards.append(guard(file_guard[0], file_guard[1], file_guard[2], file_guard[3:]))
            # taking indexes from the list and using 3: to get the movements and sending it to a different list them.
            read_guard.close()
            # closing the file
        except Exception as error_1:
            # giving an exception.
            print(error_1)

            # defining get_grids.

    def get_grid(self):

        # using a for loop to check if the item is in the range of length of the list.
        for item in range(len(self.data_guards)):
            # calling the data_list and then calling the indexes of item 0 and item 1 which is the row and col respectively.
            self.data_list_to_append[(guard.get_location(self.data_guards[item])[0])][(guard.get_location(self.data_guards[item])[1])] = "G"

        return self.data_list_to_append

    # defining get_guards and returning the list which has my guards.
    def get_guards(self):
        return self.data_guards

    # defining update_player which has direction as a parameter.
    def update_player(self, direction):
        col_1 = 0
        col_2 = 0
        row_1 = 0
        row_2 = 0
        # giving empty values to the rows and cols to use them further.
        # checking that the points and sub are index 0 and 1 in the data_list and then using them to check further.
        for sub, points in enumerate(self.data_list_to_append):
            # checking the values of "p" in points adn then P is the start position.
            if "P" in points:
                row_1 = sub
                row_2 = sub
                # giving the value of row col and the variable to which I later gave the value of col and row to sub.
                # gives the val of index P to col_1 because that would be the place where the player is.
                col_1 = points.index("P")
                col_2 = points.index("P")

                break


        # checking that is the direction is U then the player has to go up.
        if direction == "U":
            # getting the index of row and col form the list and keeping it '' to make sure its open.
            self.data_list_to_append[row_1][col_1] = " "
            # row =row-1 says that it hs to go up because the row decreases by one in that.
            row_1 = row_1 - 1
            self.win_point = self.data_list_to_append[row_1][col_1]
            # giving the value to a variable.

            if self.data_list_to_append[row_1][col_1] == "#":
                # checking if the next index is a wall then the position should be the same as before.
                self.data_list_to_append[row_2][col_2] = "P"
                self.row_1 = row_2
                self.col_1 = col_2
            else:
                # if that is not a wall then the player goes to next position.
                self.data_list_to_append[row_1][col_1] = "P"
                self.row_1 = row_1
                self.col_1 = col_1






        elif direction == "D":

            self.data_list_to_append[row_1][col_1] = " "
            row_1 = row_1 + 1
            self.win_point = self.data_list_to_append[row_1][col_1]

            if self.data_list_to_append[row_1][col_1] == "#":
                # checking if the next index is a wall then the position should be the same as before.

                self.data_list_to_append[row_2][col_2] = "P"
                self.row_1 = row_2
                self.col_1 = col_2

            else:
                self.data_list_to_append[row_1][col_1] = "P"
                self.row_1 = row_1
                self.col_1 = col_1

                # if that is not a wall then the player goes to next position.

        elif direction == "R":
            self.data_list_to_append[row_1][col_1] = " "
            col_1 = col_1 + 1
            self.win_point = self.data_list_to_append[row_1][col_1]
            if self.data_list_to_append[row_1][col_1] == "#":
                # checking if the next index is a wall then the position should be the same as before.

                self.data_list_to_append[row_2][col_2] = "P"
                self.row_1 = row_2
                self.col_1 = col_2
            else:

                self.data_list_to_append[row_1][col_1] = "P"
                # if that is not a wall then the player goes to next position.
                self.row_1 = row_1
                self.col_1 = col_1

        elif direction == "L":
            # the player goes Left when L arrives.
            self.data_list_to_append[row_1][col_1] = " "
            col_1 = col_1 - 1
            # col should be decreased as when we go left then it goes left.

            self.win_point = self.data_list_to_append[row_1][col_1]
            # giving the win point the values of row and col.

            if self.data_list_to_append[row_1][col_1] == "#":
                # checking if the next index is a wall then the position should be the same as before.

                self.data_list_to_append[row_2][col_2] = "P"
                self.row_1 = row_2
                self.col_1 = col_2
            else:

                self.data_list_to_append[row_1][col_1] = "P"
                # if that is not a wall then the player goes to next position.
                self.row_1 = row_1
                self.col_1 = col_1
        # giving the val to self


    def update_guards(self):
        for items in self.data_guards:
            guard.move(items, self.data_list_to_append)

    # updating the values by using a loop which has the point and the item and then calling the guard then calling move and then updating the index.

    def player_wins(self):

        if self.win_point == "E":
            return True

    # player wins when he reaches E that is exit.  win point is the position of the player.

    def player_loses(self):
        for player in self.data_guards:
            # in outcome, I call the enemy range then check the player row and col.
            outcome = guard.enemy_in_range(player, self.row_1, self.col_1)
            # player loses when the player is in attack range of the guard.
            if outcome == True:
                # the outcome is true when this is the case.
                return True


# making a class guard and then defining init in it.
class guard:

    def __init__(self, row, col, attack_range, movements):
        self.row = int(row)
        self.col = int(col)
        self.attack_range = int(attack_range)
        self.movements = list(movements)
        self.Grid = []
        self.current_grid = []
        # making empty lists and updating rows, cols and attack range as int.
# defining get_location and returning row and col in it.


    def get_location(self):
        return int(self.row), int(self.col)

    def move(self, current_grid):
        # defining move in which current grid is set.
        self.current_grid = current_grid
# guard_row and col is made as self here to ensure the code doesn't give any error.
        guard_row = self.row
        guard_col = self.col
# using a loop in which is the item is in the range of length of movements,i.e, the guard movement, it runs.
        for item in range(len(self.movements)):
            course_of_action = self.movements[item]
            # now the course of action changes everytime, and it picks the current element from the movement.
            print(course_of_action)
            # now telling the movement and if the current grid is a space it should be popped.
            if course_of_action == "U":
                current_grid[guard_row][guard_col] = " "
                # popping the space
                self.movements.pop(item)
                self.movements.append("U")
                # appending it to movements
                self.row = self.row - 1
                # securing the next movement by using the row and col

                if current_grid[self.row][self.col] == "#":
                    # if the current grid is a wall then
                    self.col = self.row + 1
                    return tuple((int(self.row), int(self.col)))
                else:
                    return tuple((int(self.row), int(self.col)))
                # if not then it returns a tuple of row and col

            elif course_of_action == "D":
                current_grid[guard_row][guard_col] = " "
                self.movements.pop(item)
                # popping the space
                self.movements.append("D")
                # appending it to movements
                self.row = self.row + 1
                # securing the next movement by using the row and col

                if current_grid[self.row][self.col] == "#":
                    self.col = self.row - 1
                    # if the current grid is a wall then
                    return tuple((int(self.row), int(self.col)))
                else:
                    # if not then it returns a tuple of row and col
                    return tuple((int(self.row), int(self.col)))



            elif course_of_action == "R":
                current_grid[guard_row][guard_col] = " "
                self.movements.pop(item)
                # popping the space
                self.movements.append("R")
                # appending it to movements
                self.col = self.col + 1
                # securing the next movement by using the row and col

                if current_grid[self.row][self.col] == "#":
                    self.col = self.col - 1
                    # if the current grid is a wall then
                    return tuple((int(self.row), int(self.col)))
                else:
                    return tuple((int(self.row), int(self.col)))
                # if not then it returns a tuple of row and col

            elif course_of_action == "L":
                current_grid[guard_row][guard_col] = " "
                self.movements.pop(item)
                # popping the space
                self.movements.append("L")
                # appending it to movements
                self.col = self.col - 1
                # securing the next movement by using the row and col

                if current_grid[self.row][self.col] == "#":
                    self.col = self.col + 1
                    # if the current grid is a wall then
                    return tuple((int(self.row), int(self.col)))
                else:
                    return tuple((int(self.row), int(self.col)))
                # if not then it returns a tuple of row and col

    def enemy_in_range(self, enemy_row, enemy_col):
        # not the enemy range is defined and the enemy col and enemy row subtract the current row and col

        history_row = int(abs(enemy_row - self.row))
        history_col = int(abs(enemy_col - self.col))
        left_out = history_row + history_col
# left out is the position of player ,and it needs to be outside the attack range.

        if left_out <= self.attack_range:
            return True

        else:
            return False
