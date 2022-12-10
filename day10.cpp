// Naod Philemon
// 12/10/2022

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int part1() {
  ifstream file("day10-input.txt");
  int X = 1, cycle = 0, sum = 0, check = 20;

  string line;
  while (getline(file, line)) {
    if (cycle > 220)
      break;

    cycle++;
    if (cycle % check == 0) {
      sum += cycle * X;
      check += 40;
    }

    if (line != "noop") {
      cycle++;
      if (cycle % check == 0) {
        sum += cycle * X;
        check += 40;
      }
      X += stoi(line.substr(line.find(" ")));
    }
  }

  return sum;
}

void draw(int cycle, int X) {
  if ((cycle % 40 - 1) <= X + 1 && (cycle % 40 - 1) >= X - 1) {
    cout << "#";
  } else {
    cout << ".";
  }
  if (cycle % 40 == 0)
    cout << endl;
}

void part2() {
  ifstream file("day10-input.txt");
  int X = 1, cycle = 0;

  string line;
  while (getline(file, line)) {
    cycle++;
    draw(cycle, X);

    if (line != "noop") {
      cycle++;
      draw(cycle, X);
      X += stoi(line.substr(line.find(" ")));
    }
  }
}

int main() {
  cout << "Part 1 " << part1() << endl;
  cout << "Part 2 " << endl;
  part2();

  return 0;
}
