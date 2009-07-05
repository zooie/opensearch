
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.store.FSDirectory;

public class Index {

  public static void main(String[] args) throws IOException {

    IndexWriter indexWriter = new IndexWriter(FSDirectory.getDirectory("index"),
                                              new StandardAnalyzer(),
                                              IndexWriter.MaxFieldLength.LIMITED);

    Scanner scan = new Scanner(new File("../ohsumed.flat"));

    while (scan.hasNextLine()) {
      String line = scan.nextLine().trim();
      String[] data = line.split("\t");
      Document doc = new Document();
      doc.add(new Field("id", data[0], Field.Store.YES, Field.Index.NO));
      doc.add(new Field("content", data[1], Field.Store.NO, Field.Index.ANALYZED));
      indexWriter.addDocument(doc);
    }

    //indexWriter.optimize();
    indexWriter.close();

    scan.close();
  }

}
