#include <iostream>

void showMenu(); // Here you need to name your function without a definition. The definition of what the function does is at the bottom.


//do not pay attention to case 4 in this program. That is something I am working on to add different users with different balances etc.


int main() {

	// check balance, deposit, withdraw, menu
	int option;
	double balance=1000;

	do
	{

		// menu function call to show menu until user enter number 5 to exit program
		showMenu();

		// user input option
		std::cout << "Option: ";
		std::cin >> option;
		system("cls"); //clears console for a more clean look

		// switch case to decide what to show depending on the option chose
		switch (option)
		{
		case 1: std::cout << "Balance is $" << balance << std::endl;
			break;

		case 2: std::cout << "Deposit amount: $";
			double depositAmount;
			std::cin >> depositAmount;
			balance += depositAmount;
			std::cout << "New balance is: $" << balance << std::endl;
			break;

		case 3: std::cout << "Withdraw amount: $";
			double withdrawAmount;
			std::cin >> withdrawAmount;

			if (withdrawAmount <= balance)
			{
				balance -= withdrawAmount;
				std::cout << "New balance is: $" << balance << std::endl;
				break;
			}
			else
			{
				std::cout << "Insufficient Funds!" << std::endl;
				break;
			}
		/*case 4: std::cout << "Amount to transfer: $";
			double transferAmount;
			std::cin >> transferAmount;

			if (balance < transferAmount)
			{
				std::cout << "Insufficient Funds!" << std::endl;
				break;
			}
			else
			{
				std::cout << "Enter account number to transfer funds to: ";
				std::cin >> userPin;
				if (userPin == 123)
				{
					ptr2 += transferAmount;
					balance = ptr1 - transferAmount;
					std::cout << "Transfer Successful!" << std::endl;
					break;
				}
			}*/
		case 5: std::cout << "Thanks for using our ATM. Goodbye!" << std::endl;
			break;


		default: std::cout << "Invalid option!" << std::endl;
			break;
		}

	} while (option != 5);


}

//  recommended way of writing functions with definition after main()


void showMenu()
{
	std::cout << "**********Menu**********" << std::endl;
	std::cout << "1. Check Balance" << std::endl;
	std::cout << "2. Deposit" << std::endl;
	std::cout << "3. Withdraw" << std::endl;
	/*std::cout << "4. Transfer Funds" << std::endl;*/
	std::cout << "5. Exit" << std::endl;
	std::cout << "************************" << std::endl;
}