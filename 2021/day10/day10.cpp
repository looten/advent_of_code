#include <fstream>
#include <iostream>
#include <stack>
#include <string>
#include <math.h>
#include <vector>

//const std::string &filename =
    //"/home/looten/workspace/advent_of_code/2021/day10/test_data.txt";
 const std::string& filename =
 "/home/looten/workspace/advent_of_code/2021/day10/input.txt";

void read_file(std::string &buffer) {
  std::string tmp;
  std::cout << "reading file" << std::endl;
  std::ifstream f(filename);
  f.seekg(0, std::ios::end);
  tmp.resize(f.tellg());
  f.seekg(0);
  f.read(tmp.data(), tmp.size());
  buffer = tmp.data();
}

char get_expected(const char &top) {
  switch (top) {
    case '(':
      return ')';
    case '[':
      return ']';
    case '{':
      return '}';
    case '<':
      return '>';
    default:
      break;
  }
  return 'x';
}

bool verify_ending(const char &ending, std::stack<char> &stack) {
  if (get_expected(stack.top()) == ending) {
    stack.pop();
    return true;
  }
  return false;
}

int fix_ending(std::stack<char> &stack) {
  int ret = 0;
  char val = get_expected(stack.top());
  switch (val) {
    case ')':
      ret = 1;
      break;
    case ']':
      ret = 2;
      break;
    case '}':
      ret = 3;
      break;
    case '>':
      ret = 4;
      break;
    default:
      std::cout << " hmm??" << std::endl;
      break;
  }
  return ret;
}

void check_syntax(const std::string &data) {
  const std::string ending_chars = "]})>";
  std::stack<char> stack;
  std::vector<long long> scores;
  long long score = 0;
  bool corrupt = false;

  for (auto c : data) {
    if (c == '\n') {
      score = 0;
      if (!corrupt) {
        while (!stack.empty()) {
          int current = fix_ending(stack);
          score *= 5;
          score += current;
          stack.pop();
        }
      scores.push_back(score);
      } else {
        while (!stack.empty()) {
          stack.pop();
        }
      }
      corrupt = false;
      continue;
    }

    if (ending_chars.find(c) != std::string::npos && !corrupt) {
      if (!verify_ending(c, stack)) {
        corrupt = true;
        while (!stack.empty()) {
          stack.pop();
        }
      }
    } else {
      stack.push(c);
    }
  }

  std::sort(scores.begin(), scores.end());
  int middle = floor(scores.size() / 2);

  std::cout << "Score: " << scores.at(middle) << std::endl;
}

int main() {
  std::string buffer;
  read_file(buffer);
  check_syntax(buffer);
}
