import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import org.apache.lucene.search.Query;
import org.apache.lucene.search.Searcher;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.document.Document;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.queryParser.QueryParser;
import org.apache.lucene.queryParser.ParseException;
import org.apache.lucene.analysis.standard.StandardAnalyzer;

public class Search {

    public static void main(String[] args) throws IOException, ParseException {
        String queryString;
        Scanner scan = new Scanner(new File("../queries.txt"));

        IndexReader idx = IndexReader.open("index");
        Searcher searcher = new IndexSearcher(idx);
        QueryParser qp = new QueryParser("content", new StandardAnalyzer());

        while (scan.hasNextLine()) {
          queryString = scan.nextLine().trim();

          Query query = qp.parse(queryString);
          TopDocs results = searcher.search(query, null, 10);
          for (ScoreDoc sd : results.scoreDocs) {
            Document doc = searcher.doc(sd.doc);
            System.out.println(queryString + "  " + doc.get("id"));
          }
        }

        idx.close();
        scan.close();

    }
}
