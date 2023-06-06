#include<iostream>
#include <cstdio>
#include "TTree.h"
#include "TFile.h"

using namespace std;

int main() {
  TFile *f = new TFile("myfile.root");
  TTree *T = (TTree*)f-> Get("T");
    


  return 0; // end of function main
}