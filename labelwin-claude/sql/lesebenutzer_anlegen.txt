/* =====================================================================
   Labelwin-Plugin fuer Claude: Lese-Benutzer anlegen
   ---------------------------------------------------------------------
   Ausfuehren in SQL Server Management Studio (SSMS) mit einem
   Administrator-Konto (sysadmin bzw. securityadmin + db_owner).

   1. Die drei Werte im Abschnitt EINSTELLUNGEN anpassen.
   2. Mit F5 ausfuehren.
   3. Benutzer und Passwort in labelwin.env eintragen.

   Der Benutzer bekommt NUR Leserechte (db_datareader).
   Das Skript kann gefahrlos mehrfach ausgefuehrt werden.
   Moeglichst gegen eine Test-/Kopie-Datenbank verwenden.
   ===================================================================== */

SET NOCOUNT ON;

/* ---------- EINSTELLUNGEN -------------------------------------------- */
DECLARE @Benutzer  sysname       = N'claude_ro';
DECLARE @Passwort  nvarchar(128) = N'HIER_STARKES_PASSWORT_EINTRAGEN';
DECLARE @Datenbank sysname       = N'projdat';   -- Wert "sqldatenbank" aus global.ini
/* --------------------------------------------------------------------- */

DECLARE @sql nvarchar(max);
DECLARE @qb  nvarchar(300) = QUOTENAME(@Benutzer);

IF @Passwort = N'HIER_STARKES_PASSWORT_EINTRAGEN' OR LEN(@Passwort) < 12
BEGIN
    RAISERROR(N'Bitte ein eigenes, starkes Passwort (mind. 12 Zeichen) eintragen.', 16, 1);
    RETURN;
END;

IF DB_ID(@Datenbank) IS NULL
BEGIN
    RAISERROR(N'Datenbank %s nicht gefunden. Namen pruefen.', 16, 1, @Datenbank);
    RETURN;
END;

/* 1. Server-Login anlegen (falls noch nicht vorhanden) */
IF SUSER_ID(@Benutzer) IS NULL
BEGIN
    SET @sql = N'CREATE LOGIN ' + QUOTENAME(@Benutzer)
             + N' WITH PASSWORD = ' + QUOTENAME(@Passwort, N'''')
             + N', DEFAULT_DATABASE = ' + QUOTENAME(@Datenbank)
             + N', CHECK_POLICY = ON;';
    EXEC sys.sp_executesql @sql;
    PRINT N'Login angelegt: ' + @Benutzer;
END
ELSE
    PRINT N'Login existiert bereits: ' + @Benutzer + N' (Passwort wurde NICHT geaendert)';

/* 2. Datenbank-Benutzer anlegen und NUR Leserechte geben */
SET @sql = N'USE ' + QUOTENAME(@Datenbank) + N';
IF USER_ID(@b) IS NULL
    EXEC(N''CREATE USER '' + @qb + N'' FOR LOGIN '' + @qb + N'';'');
EXEC(N''ALTER ROLE db_datareader ADD MEMBER '' + @qb + N'';'');';
EXEC sys.sp_executesql @sql, N'@b sysname, @qb nvarchar(300)', @b = @Benutzer, @qb = @qb;

PRINT N'Fertig: ' + @Benutzer + N' hat Leserechte auf ' + @Datenbank + N'.';
PRINT N'Jetzt LW_DB_USER und LW_DB_PASSWORD in labelwin.env eintragen.';
GO

-- =====================================================================
--  ALTERNATIVE ohne Passwort: Windows-Anmeldung
-- ---------------------------------------------------------------------
--  Statt eines SQL-Benutzers eine Windows-/AD-Gruppe berechtigen, z.B.
--  FIRMA\Labelwin-Claude-Lesen. Wer in der Gruppe ist, kann lesen.
--  In labelwin.env dann LW_DB_USER und LW_DB_PASSWORD leer lassen und
--  LW_DB_TRUSTED=1 eintragen.
--
--  Zum Verwenden: Gruppe und Datenbank im Block unten anpassen,
--  nur die Zeilen zwischen /* und */ markieren und F5 druecken.
-- =====================================================================
/*
USE [projdat];
IF SUSER_ID(N'FIRMA\Labelwin-Claude-Lesen') IS NULL
    CREATE LOGIN [FIRMA\Labelwin-Claude-Lesen] FROM WINDOWS;
IF USER_ID(N'FIRMA\Labelwin-Claude-Lesen') IS NULL
    CREATE USER [FIRMA\Labelwin-Claude-Lesen] FOR LOGIN [FIRMA\Labelwin-Claude-Lesen];
ALTER ROLE db_datareader ADD MEMBER [FIRMA\Labelwin-Claude-Lesen];
*/
