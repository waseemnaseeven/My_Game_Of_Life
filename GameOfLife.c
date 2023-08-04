#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

const int	WIDTH = 9;
const int	HEIGHT = 10;
const int	TRUE = 1;
const int	FALSE = 0;

/* creation du tableau avec des cellules vivantes 'O' etablies de manière aleatoire */
void	fill_array_randomly(int board[HEIGHT][WIDTH])
{
    int i, j, num;
    srand((unsigned)time(NULL)); 
    for(i =1; i <HEIGHT ; i++)
        for(j=1; j <WIDTH ;j++)
        {
            num = rand()%3; 
            if (num == 1)
                board[i][j] = 'O';
            else board[i][j] = '.';
        }
}

/* affichage du tableau */
void	display_2D_array(int board[HEIGHT][WIDTH])
{
	int rows;
	int cols;
    	for (rows = 1; rows <HEIGHT; rows++)
    	{
        	for(cols = 1; cols <WIDTH; cols++)
            		printf ("%3c", board[rows][cols]);
		printf("\n");
	}
}

/* etablissement des règles élémentaires  : 
	- si la cellule vivante possèdent 2 ou 3 trois cellules voisines vivantes
	  la cellule continue de vivre, sinon elle meurt
*/
void	count_neighbors(int board[HEIGHT][WIDTH])
{
	int	neighbors;
	int	rows;
	int	cols;
	int	a, b;

	for (rows = 1; rows < HEIGHT; rows++)
	{
		for (cols = 1; cols < WIDTH; cols++)
		{
			neighbors = 0;
			if (board[rows][cols] == 'O')
			{
				for (a = -1; a < 3; a++)
				{
					for (b = -1; b < 3; b++)
					{
						if ((a == rows) && (b == cols))
							neighbors = neighbors;
						else if ((board[rows][cols] == 'O') || (board[rows][cols] == 1) || (board[rows][cols] == 0))
							neighbors++;
						if ((neighbors == 2) || (neighbors == 3))
							board[rows][cols] = 1; // vivant
						else
							board[rows][cols] = 0; // die
					}
				}
			}
		}
	}
}

void	check_newborns(int board[HEIGHT][WIDTH])
{
	int neighbors;
    	int rows;
    	int cols;
    	int a, b;
    	for (rows =1; rows <HEIGHT -1; rows++)
    	{
        	for (cols = 1; cols <WIDTH -1; cols ++)
        	{
        	    neighbors = 0;
            		if (board[rows][cols] == '.')
			{
				if ((rows -1 == rows) && (cols -1 == cols))
					neighbors = neighbors;
				else if ((board[rows -1][cols -1] == 'O') || (board[rows -1][cols -1] == 1) || (board[rows -1][cols -1] == 0))
					neighbors++;
				if (neighbors == 3)
					board[rows][cols] = 2; // newborn
			}
		}
	}
}

void	new_generation(int board[HEIGHT][WIDTH])
{
	int	rows;
	int	cols;

	for (rows = 1; rows < HEIGHT-1; rows++)
	{
		for (cols = 1; cols < WIDTH; cols++)
		{
			if (board[rows][cols] == 1)
				board[rows][cols] = 'O';
			else if (board[rows][cols] == 2)
				board[rows][cols] = 'O';
			else
				board[rows][cols] = '.';
		}
	}
}

/*void	playgame(int board[HEIGHT][WIDTH], int num_generation)
{
	for (int i = 1; i <= num_generation; i++)
	{
		system("cls");
		count_neighbors(board);
		check_newborns(board);
		new_generation(board);
	}


}*/

void	auto_mode(int board[HEIGHT][WIDTH])
{
	int	num_generation;

	num_generation = 0;
	fill_array_randomly(board);
	display_2D_array(board);
	printf("\n");
	fill_array_randomly(board);
	display_2D_array(board);
	count_neighbors(board);
	check_newborns(board);
	new_generation(board);
	//printf("\nSelect a number of generation: ");
	//scanf("%i", &num_generation);

	//playgame(board, num_generation);
}

int main(int ac, char **av)
{
	int	board[HEIGHT][WIDTH];
	(void) ac;
	(void) av;

	auto_mode(board);
}
