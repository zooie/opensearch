/** @file simplesearch.cc
 * @brief Simple command-line search utility.
 *
 * See "quest" for a more sophisticated example.
 */
/* Copyright (C) 2007 Olly Betts
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
 */

#include <xapian.h>

#include <fstream>
#include <iostream>
#include <string>

#include <stdlib.h> // For exit().

using namespace std;

int main() {
    // Open the database for searching.
    Xapian::Database db("medindex");

    // Start an enquire session.
    Xapian::Enquire enquire(db);

    ifstream f("/Users/viksi/git/opensearch/exp/software/ohsumed/queries.txt");
    string query_string;

    Xapian::QueryParser qp;
    qp.set_database(db);
    qp.set_default_op(Xapian::Query::OP_OR);
    Xapian::Query query;
    Xapian::MSet matches;

    while (!f.eof()) {
      getline(f, query_string);
      query = qp.parse_query(query_string);

      // Parse the query string to produce a Xapian::Query object.
      //Xapian::Stem stemmer("english");
      //qp.set_stemmer(stemmer);
      //qp.set_stemming_strategy(Xapian::QueryParser::STEM_SOME);
      //cout << "Parsed query is: " << query.get_description() << endl;

      // Find the top 10 results for the query.
      enquire.set_query(query);
      matches = enquire.get_mset(0, 10);

      // Display the results.

      for (Xapian::MSetIterator i = matches.begin(); i != matches.end(); ++i) {
        cout << query_string << " " << i.get_document().get_value(0) << "\n";
        //cout << query_string << " " << i.get_document().get_docid() << "\n";
      }
  }
  f.close();
}
