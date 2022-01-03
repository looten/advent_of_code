#include <fstream>
#include <iostream>
#include <stack>
#include <string>

//const std::string &filename =
  //  "/home/looten/workspace/advent_of_code/2021/day10/test_data.txt";
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

  if (0)
  {
  std::string line = "";
  for (auto c : tmp) {
    line += c;
    if (c == '\n') {
      //std::cout << "weird size?" << std::endl;
      if (line.size() % 2 != 0) {
        std::cout << "remove due to weird size" << std::endl;
        size_t pos = tmp.find(line);
        if (pos != std::string::npos)
          tmp.erase(pos, line.length());
      }
      line = "";
    }
  }
  }
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
      std::cout << "What? get expected\n";
      exit(0);
  }
  return 'x';
}


int verify_ending(const char &ending, std::stack<char> &stack) {
  int ret = 0;
  const char expected = get_expected(stack.top());
  
  if (expected != ending) {
    std::cout << "incorrect "<< std::endl;
    std::cout << "expected " << expected<< std::endl;
    std::cout << "ending " << ending<< std::endl;
    switch (ending) {
      case ')':
        ret = 3;
        break;
      case ']':
        ret = 57;
        break;
      case '}':
        ret = 1197;
        break;
      case '>':
        ret = 25137;
        break;
      default:
        std::cout << " hmm??" << std::endl;
        break;
    }
  }
  else
  {
    stack.pop();
  }

  return ret;
}

void check_syntax(const std::string &data) {
  std::stack<char> stack;
  const std::string ending_chars = "]})>";

  int illegal_score = 0;
  int current = 0;
  bool find_new_line = false;

  for (auto c : data) {
    // std::cout << line << std::endl;
    if (c == '\n') {
      std::cout << "new row" << std::endl;
      if (!find_new_line)
      {
        std::cout << "incomplete row" << std::endl;
      }
      else{
        illegal_score += current;
      }
      find_new_line = false;
      current = 0;
      while (!stack.empty()) {
        stack.pop();
      }
      std::cout << "sum: " <<  illegal_score << std::endl;
      continue;
    }

    if (find_new_line) {
      continue;
    }


    // ending char found
    if (ending_chars.find(c) != std::string::npos) {
      current = verify_ending(c, stack);
      
      if (current > 0) {
        std::cout << "corrut line" << std::endl;
        find_new_line = true;
      }
    }
    else
    {
      stack.push(c);
    }




  }
  std::cout << "Score: " << illegal_score<< std::endl;
}



int main() {
  std::string buffer;
  read_file(buffer);
  std::cout << "line:\n" << buffer << std::endl;
  check_syntax(buffer);
}