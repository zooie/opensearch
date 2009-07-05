
#include <xapian.h>

#include <iostream>
#include <fstream>
#include <string>

#include <stdlib.h>

using namespace std;

void onesplit(const string &input, const string &sep, string* tokens) {
    string::size_type pos = input.find(sep, 0);
    tokens[0] = input.substr(0, pos);
    tokens[1] = input.substr(pos+1, string::npos);
}

int main() {
  Xapian::WritableDatabase db("medindex", Xapian::DB_CREATE_OR_OPEN);

  //Xapian::Stem stemmer("none");
  //indexer.set_stemmer(stemmer);

  ifstream f("/Users/viksi/git/opensearch/exp/software/ohsumed/ohsumed.flat");
  string line;

  string tokens[2];

  db.begin_transaction(0);

  while (!f.eof()) {
    getline(f, line);
    onesplit(line, "\t", tokens);
    Xapian::TermGenerator indexer;
    Xapian::Document doc;
    //doc.set_data(tokens[1]);
    doc.add_value(0, tokens[0]);

    indexer.set_document(doc);
    //indexer.index_text(tokens[1]);
    indexer.index_text_without_positions(tokens[1]);

    db.add_document(doc);
  }

  db.commit_transaction();

  f.close();
}
